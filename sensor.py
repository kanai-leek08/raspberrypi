# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import subprocess
import pexpect

class LineNotify:
  def send(self):
    ACCESS_TOKEN = "取得したトークンを入力してください"
    MESSAGE = "防犯システムが作動しました。 写真URL：http://" + HOST + "/~students/" + students_dir + "/" + server_filename
    command = "curl"
    command = command + " -X POST"
    command = command + " -H 'Authorization: Bearer " + ACCESS_TOKEN + "'"
    command = command + " -F 'message=" + MESSAGE + "'"
    command = command + " https://notify-api.line.me/api/notify"
    subprocess.call(command, shell=True)

class Server:
  def scp(self):
    ID = ''
    PASSWORD = ''
    HOST = ''
    DIR = ''

    students_dir = 'ABA7132/images'
    local_filename = 'capture.jpg'
    server_filename = 'capture.jpg'
    scp_command = 'scp ' + local_filename
    scp_command = scp_command + ' ' + ID + '@' + HOST + ':' + DIR + '/' + students_dir + '/' + server_filename

    command = pexpect.spawn(scp_command)
    command.expect('(?i)password')
    command.sendline(PASSWORD)
    command.expect(pexpect.EOF)

class Voice:
  def run(self):
    file = "/home/pi/alert.wav"
    cmd = "aplay " + file
    subprocess.call(cmd, shell=True)

class Camera:
  def take(self):
    cmd = "raspistill -t 100 -o " + "capture.jpg"
    subprocess.call(cmd, shell=True)


class Sensor:

  sensor_pin = 4
  light_pin = 18

  def watch(self):

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.sensor_pin, GPIO.IN)
    GPIO.setup(self.light_pin, GPIO.OUT)

    for i in range(1, 61):
      if (GPIO.input(self.sensor_pin) == GPIO.HIGH):
        print("人体を感知しました")
        Voice().run()
	GPIO.output(self.light_pin, GPIO.HIGH)
	Camera().take()
	Server().scp()
      else:
        print("人体を感知していません")
	GPIO.output(self.light_pin, GPIO.LOW)
      time.sleep(1)


Sensor().watch()
