> 
1.The installation executable of the JDK is a zipped file, so just unzip it with 7z to any folder you want.
2.Go to the directory .rsrc/1033/JAVA_CAB10/.
3.The only file there is 111, which is also a zipped file containing tools.zip. Unzip it to get tools.zip.
4.So now perform the original unpack process, by unzipping tools.zip to your desired java installation path.
5.Open a windows command prompt and run: for /r %i in (*.pack) do .\bin\unpack200.exe -r -v %i %~pi%~ni.jar
The unpack200 program complains about garbage at the end of the files, but the unpacked jars are tested ok by 7z.
6.Java source src.zip is within the file 110 located inside .rsrc/1033/JAVA_CAB9.
By the way, updating 101 only contains the tools.zip file and can be installed with the previous unpack method.
