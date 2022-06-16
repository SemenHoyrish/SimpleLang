if [ -d "./build" ]
then

    if [ "$(ls -A './build')" ]; then
      echo "Directory 'build' already exists and not empty. Are you sure to remove all its content? y/n: "
      read ans
      if [ $ans = "y" ]
      then
        rm ./build/* -r
      else
        exit 0
      fi
    else
      echo "Directory is Empty. "
    fi
else
    mkdir build
    echo "Directory 'build' created. "
fi

cp main.py ./build/main.py
cd ./build
# pyinstaller -F main.py -n sl.exe --paths "C:\Python310\Lib\site-packages" --hiddenimport websockets --hiddenimport websockets.legacy --hiddenimport websockets.legacy.server
pyinstaller -F main.py -n sl.exe
cp ./dist/sl.exe ../sl.exe

echo "Enter for exit"
read for_exit
