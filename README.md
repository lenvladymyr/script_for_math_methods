script_for_math_methods
=======================

Скрипт допилен! Теперь, чтобы им воспользоваться нужен один из дистрибутивов GNU/Linux.
Далее команды выполняются по очереди:

$sudo apt-get install git

$sudo git clone https://github.com/lenvladymyr/script_for_math_methods

$cd script_for_math_methods

$sudo apt-get install python-numpy python-scipy

$sudo python script.py


Так запускается скрипт, но там остались мои значения. Для этого открываете его в любом редакторе (vi или nano) и изменяете количество альтернатив (переменная alt), количество критериев (переменная krit) и количество весовых коэффициентов в списке w (не забывайте, что их сумма должна равняться 1). Profit!
