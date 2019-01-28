from bluetooth import *

# 블루투스 시리얼 통신 UUID
uuid = "00001101-0000-1000-8000-00805f9b34fb";

# 블루투스 시리얼 통신 준비   
server_sock=BluetoothSocket( RFCOMM );
server_sock.bind(('',PORT_ANY));
server_sock.listen(1);

port = server_sock.getsockname()[1];

advertise_service( server_sock, "serial_examples", uuid);
	
# 클라이언트가 연결될 때까지 대기
print("스마트폰 연결 대기중");
client_sock, client_info = server_sock.accept();
print("스마트폰 연결 완료", client_info);

while True:          
	try:
		data = client_sock.recv(1024);
		if len(data) == 0: break;
		str = data.decode('utf-8');
		print("전송 받은 문자열 : [%s]" % str);
	except IOError:
		print("연결 종료");
		client_sock.close();
		server_sock.close();
		break
		
	except KeyboardInterrupt:
		client_sock.close();
		server_sock.close();
		print("프로그램 종료");
		break

