char serialData;
int light=8;//Output pin for light
int fan=7;//Output pin for fan
int tv=6;//Output pin for tv
int ac=5;//Output pin for ac

void setup() {
  // put your setup code here, to run once:
  pinMode(light,OUTPUT);
  pinMode(fan,OUTPUT);
  pinMode(tv,OUTPUT);
  pinMode(ac,OUTPUT);
  
  Serial.begin(9600);
  
  digitalWrite(light,LOW);
  digitalWrite(fan,LOW);
  digitalWrite(tv,LOW);
  digitalWrite(ac,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    serialData=Serial.read(); //read data send from pyremote
    Serial.print(serialData);
    if (serialData == 'A'){
      digitalWrite(light,HIGH);//Turn on light
    }
    else if(serialData== 'a'){
      digitalWrite(light,LOW);//Turn off light
    }
    else if (serialData == 'B'){
      digitalWrite(fan,HIGH);//Turn on fan
    }
    else if (serialData == 'b'){
      digitalWrite(fan,LOW);//Turn off fan
    }
    else if(serialData== 'C'){
      digitalWrite(tv,HIGH);//Turn on TV
    }
    else if (serialData == 'c'){
      digitalWrite(tv,LOW);//Turn of TV
    }
    else if (serialData == 'D'){
      digitalWrite(ac,HIGH);//Turn on AC
    }
    else if (serialData == 'd'){
      digitalWrite(ac,LOW);//Turn off AC
    }
    else if (serialData == 'X'){
      digitalWrite(light,HIGH);
      digitalWrite(fan,HIGH);
      digitalWrite(tv,HIGH);
      digitalWrite(ac,HIGH);//Turn on everything
    }
    else if(serialData == 'x'){
      digitalWrite(light,LOW);
      digitalWrite(fan,LOW);
      digitalWrite(tv,LOW);
      digitalWrite(ac,LOW);//Turn off everything
    }
  }
}
