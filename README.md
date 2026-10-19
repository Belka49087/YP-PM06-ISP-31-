# Программный комплекс «Калькулятор прогрессий и подсистема бэкапа»

Консольно-графическое программное обеспечение на языке Python, разработанное в рамках учебной практики по профессиональному модулю ПМ 06 «Сопровождение информационных систем» (Вариант 22).

## Руководство пользователя (Russian Language)

Программа предназначена для высокоточного нахождения значения n-го члена арифметической или геометрической прогрессии по первому члену, шагу (знаменателю) и номеру элемента. Архитектура ИС разделена на три независимых модуля: исполнительный (`ispolnitelnie.py`), графический (`graficheskie.py`) и функциональный (`functionalnie.py`).

### Функциональные возможности
* **Интерфейс:** Полноценное графическое окно на базе встроенной библиотеки Tkinter.
* **Два режима расчетов:** Интерактивная работа через оконную форму или пакетный расчет внешних файлов конфигурации обмена (input.json / output.json).
* **Сохранение конфигураций:** Возможность записи текущих параметров расчетов в энергонезависимые профили пользователей.
* **Отказоустойчивость (ПМ 06):** Автоматическое создание полных резервных копий базы профилей в изолированный каталог backups под уникальным штампом времени (timestamp) и аварийный откат структуры ИС до последней стабильной контрольной точки.

### Системные требования
* Операционная система: Windows 10/11, macOS или Linux.
* Установленный интерпретатор Python версии 3.8 или выше.
* Не требует установки сторонних библиотек (используются встроенные модули os, json, shutil, datetime, tkinter).

### Инструкция по запуску
1. Скачайте файлы проекта в одну рабочую директорию.
2. Откройте терминал или командную строку в папке проекта и запустите главный исполнительный модуль:
   ```bash
   python ispolnitelnie.py
   ```
3. Для проведения автоматизированной верификации и запуска unit-тестов расчетного ядра выполните:
   ```bash
   python -m unittest test_prog.py
   ```

---

## User Guide (English Language)

This Python-based application features a clean three-file architecture (`ispolnitelnie.py`, `graficheskie.py`, `functionalnie.py`) and is designed to compute the n-th member of arithmetic or geometric progressions. Developed as a core assignment for the software engineering and maintenance module (Variant 22).

### Key Features
* **Graphical Interface:** Implemented using the native Python Tkinter GUI framework.
* **Dual Operating Modes:** Direct manual parameters computation via GUI window or background batch file processing (input.json / output.json).
* **Configuration Management:** Saves trackable sequence parameters into organized JSON database profiles.
* **Data Maintenance (Backup):** Automated full-point backup system that duplicates profiles into a secure backups directory using precise timestamps with one-click data restore capabilities.

### System Requirements
* Operating System: Windows 10/11, macOS, or Linux.
* Python 3.8 runtime environment or higher.

### Quick Start Guide
1. Retrieve all project source files and place them inside a single root folder.
2. Launch your terminal application in the project source path and execute the main executable module:
   ```bash
   python ispolnitelnie.py
   ```
3. To run automated verification script and validate core modules stability, execute:
   ```bash
   python -m unittest test_prog.py
   ```
