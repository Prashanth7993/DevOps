$Path = [Environment]::Getfolderpath("Desktopdirectory")
echo $Path

if (Test-Path $Path -pathtype container){
    "desktop folderExits"
} else {
    "folder doesn't exits"
}