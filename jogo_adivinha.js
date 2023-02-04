for (contador = 0; contador <3; contador ++ ){ 
    alert ("Vamos ver se voçe consegue acertar o numero!! Escolha um numero de 1 a 10.");
    
    var numero = Math.round(Math.random()*10);
    
    var chute = parseInt(prompt("Digite um numero "))
    
    if(chute == numero){
        alert("Voce acertou ... Parabens ")
       break;
    }else{
        alert("Tente mais uma vez")
    } 
}
