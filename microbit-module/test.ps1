$COMportList = [System.IO.Ports.SerialPort]::getportnames() 
ForEach ($COMport in $COMportList) { 
$temp = new-object System.IO.Ports.SerialPort $COMport 
echo $temp.PortName 
$temp.Dispose() 
}