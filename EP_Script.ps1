#------------------------------------------------------------
# Fonction de download 
#------------------------------------------------------------

function Download-Image {

    #Get json from reddit
    $argument_function0 = $args[0]
    if($nb_args -eq 2){
        $argument_function1 = $args[1]
        $path = $argument_function1
    }else{
        $y = 0
        $path = 'C:\Users\'+$user+'\Desktop\imagesEarthPornReddit'
     
        # Creat new directory on user's desktop
        New-Item -Path  $path -ItemType Directory
        Write-Output "Dossier créé."
    }

    if($argument_function0 -le 25 ){
        $request = 'https://www.reddit.com/r/EarthPorn.json'
    }elseif($argument_function0 -le 100){
        $request = 'https://www.reddit.com/r/EarthPorn.json?limite=$argument_function0'
    }else{
        $request = 'https://www.reddit.com/r/EarthPorn.json?limite=100'
    }

    $data = Invoke-WebRequest $request | ConvertFrom-Json

    #Set few paramters

    $imax = $argument_function0

    $i = 0

    $user = $env:UserName

    $wc = New-Object System.Net.WebClient

    Do{

        $i++

        $name = $path + "\image" + $i + ".jpg"
       
        $wc.DownloadFile($data.data.children[$i].data.url_overridden_by_dest, $name)
        Write-Output "$name téléchargé"

    }Until($i -eq $imax)

}


#------------------------------------------------------------
# Detection de la commande & arguments 
#------------------------------------------------------------

$nb_args = $args.Count

Write-Output "$nb_args"
$argument0 = $args[0]
if($nb_args -eq 2){
    $argument1 = $args[1]
}

if ($nb_args -eq 1 -AND $argument0 -is [int]) {
    Write-Output "1 seul argument qui est un int"
    Download-Image $argument0
}elseif ($nb_args -eq 2 -AND $argument0 -is [int]){
    if(Test-Path $argument1){
        Write-Output "Téléchargement de $argument0 images dans le répertoire $argument1"
        Download-Image $argument0 $argument1
    }else {
        Write-Output "Mauvais chemin de fichier"
    }
}elseif($nb_args -gt 2) {
    Write-Output "Trop d'argument. Démarre de script avec l'option 'help' pour plus de détail"
}elseif($nb_args -eq 1 -AND $argument0 -eq "help"){
    Write-Output "Ce script permet de télécharger des images depuis le post reddit EarthPorn"
    Write-Output "Dans le répertoire de ton entre dans l'interpreteur powershell avec la commande : Powershell.exe"
    Write-Output "Lance le avec la commande '.\EP_script.ps1 arg1 arg2'"
    Write-Output "arg1 est le nombre d'image que tu veux récupérer"
    Write-Output "arg2 est le path de destination du chemin (optionnel)"
}else{
    Write-Output "Erreur. Démarre de script avec l'option 'help' pour plus de détail"
}


