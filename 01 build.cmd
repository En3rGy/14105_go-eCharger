@echo off
set path=%path%;C:\Python27\
set PYTHONPATH=C:\Python27;C:\Python27\Lib

echo ^<head^> > .\release\log14105.html
echo ^<link rel="stylesheet" href="style.css"^> >> .\release\log14105.html
echo ^<title^>Logik - go-eCharger (14105)^</title^> >> .\release\log14105.html
echo ^<style^> >> .\release\log14105.html
echo body { background: none; } >> .\release\log14105.html
echo ^</style^> >> .\release\log14105.html
echo ^<meta http-equiv="Content-Type" content="text/html;charset=UTF-8"^> >> .\release\log14105.html
echo ^</head^> >> .\release\log14105.html

@echo on

type .\README.md | C:\Python27\python -m markdown -x tables >> .\release\log14105.html


cd ..\..
C:\Python27\python generator.pyc "14105_go-eCharger" UTF-8

xcopy .\projects\14105_go-eCharger\src .\projects\14105_go-eCharger\release /exclude:.\projects\14105_go-eCharger\src\exclude.txt

@echo Fertig.

@pause
