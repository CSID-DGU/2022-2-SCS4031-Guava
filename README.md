# 2022-2-SCS4031-Guava

---

# Project Introduction
> 도시화가 진행됨에 따라 건물의 고층화 및 밀집화로 인해 화재로 인한 피해가 나날이 증가하고 있다. 그러나, 기존의 화재 감지기는 높은 오작동율과 발화 지점 및 피구조자 정보 파악의 한계점이 존재하여 화재 사고 골든타임을 놓치는 일이 빈번하게 발생하고 있다. 이에 본 논문에서는 온도 센서, 가스 감지 센서, 레이더 센서로 구현한 일체형 화재 감지기와 IoT 플랫폼을 활용한 실시간 화재 정보 모니터링 시스템을 제안한다. 제안하는 시스템은 라즈베리파이 기반의 온도 센서와 가스 감지 센서를 이용하여 화재 감지 정확도를 높였으며, 레이더 센서를 이용한 객체 감지기를 통해 화재 발생 지점의 피구조자 인원 수를 파악한다. 측정되는 모든 데이터는 라즈베리파이 및 게이트웨이에 설치된 IoT 플랫폼인 TAS를 통해 수집되어 &Cube로 전송된다. 이 후,  &Cube에서 서버 플랫폼인 Mobius에 전달되어 최종적으로 MySQL Database에 저장되어 Grafana를 통해 웹 대시보드 형태로 시각화된다. 

# Team Members
| 팀원 | 역할 |
| ------- | ------- |
| 김성호 | IoT 플랫폼 개발, Grafana 제작  / 보고서 및 회의록 작성|
| 이경석 | 레이더 센서 구동 / 회의록 작성, 예산 관리 |
| 임혜정 | 라즈베리파이 화재 감지기 제작, IoT 플랫폼 개발 / 보고서 및 회의록 작성, ppt 제작|


# Environment
```
OS: Linux
Node JS: 19.3.0
MySQL : 8.0.22
Eclipse Mosquitto : 2.0.4
Mobius : 2.4.36
&Cube-Thyme : 2.3.2
```

# Usage
```
Step1 Mobius 구동

Step2 &Cube 구동
1. cd \nCube-Thyme-Nodejs-2.3.2
2. nano(vim) conf.js
     -> cse.host        = '모비우스 ip'; 수정
3. node thyme.js

Step3 TAS 구동
1. cd \nCube-Thyme-Nodejs-2.3.2\tas_sample\tas_co2
2. nano(vim) conf.xml 
     -> <parenthostname> 서버 ip <parenthostname> 수정
3. npm install
4. npm install node-dht-sensor
5. npm install mpc-spi-adc
6. node app.js

```
