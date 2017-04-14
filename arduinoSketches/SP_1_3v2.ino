
//Pump variables
int Mode, freq, delaySec, delayUSec;

//to be used to listen for stop instructions and read incoming data
int inStrComplete = 0;
int receivedStop = 0;

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  digitalWrite(2, LOW);
  digitalWrite(3, HIGH);

}

void loop() {

}

void serialEvent() {
  int point = 0;
  char inputString[16] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
  while (Serial.available()) {
    delay(5);
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString[point++] = inChar;
  }
  //Serial.println(inputString);
  if(inputString[0] == 's'){
    receivedStop = 1;
    inputString[1] = '\n';
    inputString[2] = '\0';
    //Serial.println("Stopping...");
    noTone(4);
    digitalWrite(2, HIGH);
    
  }else{
    //Serial.println("received pump");
    Mode = atoi(&inputString[0]);    // Call atoi function and return result
    freq = atoi(&inputString[0]+2);
    delaySec = atoi(&inputString[0]+7);
    delayUSec = atoi(&inputString[0]+12);
    digitalWrite(2, LOW);
    pump(Mode,freq,delaySec,delayUSec);
    
  }
}

void pump(int dir, int freq, int sec, int millisec){
  // Sets drive direction, depending on value of 'dir'
  if(dir == 2){
     digitalWrite(3,HIGH); 
     
  }else{
     digitalWrite(3,LOW);
  }
  // Converts pump time into milliseconds
  unsigned long t = (sec*1000)+millisec;
  
  // Redundant noTone() call, to ensure no signal on pin
  noTone(4);
  // Call tone on designated pin for designated time
  tone(4,freq,t);
  // Wait for designated time, then send 'finished' message across serial channel
  delay(t);
  Serial.println("end");
  
}
