if(get-Childitem | where-object {$_.name -like "desktop"}){
	echo "Folder exits"
else{
	echo "Folder doesn't exists"
}