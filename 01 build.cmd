@echo off
set path=%path%;C:\Python27\
set PYTHONPATH=C:\Python27;C:\Python27\Lib
@echo on

cd ..\..
C:\Python27\python generator.pyc "14105_go-eCharger" UTF-8
@REM C:\Python27\python generator.pyc "EasterDate" UTF-8

xcopy .\projects\14105_go-eCharger\src .\projects\14105_go-eCharger\release

@echo Fertig.

@pause