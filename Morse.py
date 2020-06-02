from tkinter import *
import RPi.GPIO as GPIO
import time

led=7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,GPIO.LOW)

window = Tk()
window.title("Morse Code")
window.geometry('300x60')

name = Label(window,text = 'Name:').grid(row=0)

inputName = Entry(window)
inputName.grid(row=0,column=1)
inputName.delete(0,END)

exit = Button(text = "Send Morse",command = lambda: Morse(inputName.get())).grid(row=4)
CODE = {'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'}
 
def Dot():
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(led,GPIO.LOW)
    time.sleep(0.25)

def Dash():
    GPIO.output(led,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(led,GPIO.LOW)
    time.sleep(0.5)
GPIO.cleanup()

def Morse(name):
  if len(name) > 12:
    print('Name is too long')
    window.destroy()
  inputName.delete(0,END)
  
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(led,GPIO.OUT)
  for alphabets in name:
    for sym in CODE[alphabets.upper()]:
      if sym == '.':
        Dot()
      elif sym == '-':
        Dash()
    time.sleep(1)
   
