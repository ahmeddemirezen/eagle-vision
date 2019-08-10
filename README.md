# Eagle Vision

## English

Remote controlled camera system.

## Getting Started

### Prerequisites

The necessary items for the server are available in the file, but you can install the libraries that are used against the possible situation as follows.

```
pip3 install socket

pip3 install RPi.GPIO

pip3 install adafruit-pca9685
```

### Installing

The installation will first run the "server.py" file from the host.

```
python3 /directory/server_v1.py
```

Here the user name and password will come up as the default user name: "admin" password: "123" is the form.
After logging in successfully, we will ask you to enter host and port information. You must enter the local ip address of the server computer as a host. By default, the port address is set to "6969".

Example:

```
Host=192.168.1.45
port=6969
```

After completing these operations, the order will be made via the raspberry pi card. In this section, we need to make small changes on the codes. Replace the IP address of the "client.py" file against the host variable.

```
host="192.168.1.54"
```

And at the end of the process, you can now run the "client.py" file through the terminal.

```
python3 /directory/client_v1.py
```
If you received a successful message from the server computer, everything went fine.

## Authors

* **[Ahmed Demirezen](https://github.com/ahmeddemirezen)**

## Acknowledgments

* I am thanks to [Ömer Ermiş](https://github.com/systran20) for he helped me at all of problem.

# Eagle Vision

## Türkçe

Uzaktan kontrol edilebilir kamera sistemi. 

## Kullanım Kılavuzu

### Ön Şartlar

Sunucu için gerekli öğeler dosyanın içerisinde mevcut ama olası duruma karşı kullanılan kütüphanelerin kurulumunu aşağıdaki gibi yapabilirsiniz.

```
pip3 install socket

pip3 install RPi.GPIO

pip3 install adafruit-pca9685
```

### Kurulum

Kurulum için ilk olarak ana bilgisayardan "server.py" dosyasını çalıştırmak olacaktır.

```
python3 /dizin/server_v1.py
```

Burada karşınıza kullanıcı adı ve şifre çıkacaktır bunlar varsayılan olarak kullanıcı adı:"admin" şifre:"123" şeklindedir.
Başarılı bir şekilde giriş yaptıktan sonra bizden host ve port bilgilerini girmemizi isteyecektir. Burada host olarak sunucu bilgisayarın yerel ip adresini girmeniz gerekmektedir. Varsayılan olarak port adresi "6969" olarak ayarlıdır bunu isteğinize göre yapılandırabilirsiniz.

Örneğin:

```
Host=192.168.1.54
port=6969
```

Bu işlemleri tamamladıktan sonra sıra raspberry pi kartı üzerinden yapılacak olan ayarlara. Bu kısımda kodlar üzerinde küçük değişiklik yapmamız gerekmekte. "client.py" dosyasındaki host değişkenin karşısında yazan ip adresini sunucu ip adresi ile değiştirmek.

Örneğin:

```
host="192.168.1.54"
```

Ve sonunda işlemler tamam artık "client.py" dosyasını terminal üzerinden çalıştırabilirsiniz.

```
python3 /dizin/client_v1.py 
```

Eğer sunucu bilgisayardan bağlantı başarılı şeklinde mesaj aldıysanız herşey yolunda gitmiş demektir.

## Yazarlar

* **[Ahmed Demirezen](https://github.com/ahmeddemirezen)**

## Emeği Geçenler

* Karşıma çıkan problemlerin çözümünde her zaman yardımcı olan [Ömer Ermiş](https://github.com/systran20)'e teşekkür etmeyi borç bilirim.

