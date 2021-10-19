# Geocoder
Aвторы:

Ильичев Матвей(matvey.ilichev@gmail.com)

Ревью выполнили: Анкудинов Александр

# Описание
CLI приложение, для поиска полного адреса и его координат.

# Требования

Python версии не ниже 3.6
pip install -r requirements.txt

# Запуск

python3 -m geocoder ..
- '-a|-address' + адрес - для поиска введеного 
 	- Адрес в формате:
                             '"область=обл."_'
                             '"город=гор.=г."_'
                             '"улица=ул."_'
                             '"дом=д."_'
                             '"разделители: ; , /"')
	- Пример: python3 -m geocoder -a "гор. Екатеринбург; улица Тургенева, д. 4" или python3 -m geocoder -a "г. Екатеринбург; ул. Тургенева, дом 4"
	
- -d', '-download' + город - для скачивания адресов данного города
  - Пример: python3 -m geocoder -d "Екатеринбург"
