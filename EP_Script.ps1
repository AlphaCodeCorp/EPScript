
#------------------------------------------------------------
# Detection de la commande & arguments 
#------------------------------------------------------------

$nb_args = $args.Count

if ($nb_args -eq 1 -AND $args[0] -is [int]) {
    $nb_images = $args[0]
}elseif ($nb_args -eq 2 -AND $args[0] -is [int]){
    if(Test-Path $args[1]){
        Write-Output "Téléchargement de $args[0] images dans le répertoire $arg[1]"
        Download-Image $args[0] $args[1]
    }else {
        Write-Output "Mauvais chemin de fichier"
    }
}elseif($nb_args -gt 2) {
    Write-Output "Trop d'argument. Démarre de script avec l'option 'help' pour plus de détail"
}elseif($nb_args -eq 1 -AND $args[0] -eq "help"){
    Write-Output "Ce script permet de télécharger des images depuis le post reddit EarthPorn"
    Write-Output "Lance le avec la commande '.\EP_script.ps1 arg1 arg2'"
    Write-Output "arg1 est le nombre d'image que tu veux récupérer"
    Write-Output "arg2 est le path de destination du chemin (optionnel)"
}else{
    Write-Output "Erreur. Démarre de script avec l'option 'help' pour plus de détail"
}


#------------------------------------------------------------
# Fonction de download 
#------------------------------------------------------------

function Download-Image {

    #Get json from reddit

    $request = 'https://www.reddit.com/r/EarthPorn.json'

    $data = Invoke-WebRequest $request | ConvertFrom-Json

    #Set few paramters

    $imax = $data.data.children.Length

    $i = 0

    $user = $env:UserName


    # Creat new directory on user's desktop

    $path = 'C:\Users\'+$user+'\Desktop\imagesEarthPornReddit'

    #New-Item -Path  $path -ItemType Directory


    $wc = New-Object System.Net.WebClient

    Do{

        $i++

        $name = $path + "\image" + $i + ".jpg"

        #$wc.DownloadFile($data.data.children[$i].data.url_overridden_by_dest, $name)

    }Until($i -eq $imax)

}

