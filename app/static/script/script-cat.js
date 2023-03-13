function ver(especie){
    if(especie== "perro"){
        swal({
            title: "Ectogen Max",
            text: "FÓRMULA: IMIDACLOPRID \n(1) ……………………………………………..7,60 g.\n PERMETRINA (2) ………………………………………………35,70 g.\n"+
            "BUTOXIDO DE PIPERONILO …………………………………..1 g.\n"+
            "AGENTES DE FORMULACION C.S.P. ……………….100 ml.\n\n"+
            "1) 1-[(6-Cloro-3-piridinil) metil] – 4,5-dihidro-N-nitro-1H-imidazol –2 -amina\n"+
            "2) 2,2 – dimetil-3-(2,2-diclorovinil – ciclopropil – 1 – carboxilato de 3- penoxibencilo.\n\n"+
            "ESPECIES DE DESTINO:Caninos.",
            buttons: "Ver mas"
          });
    }else if(especie=="gato"){
        swal({
            title: "Ectogen Plus",
            text:"FÓRMULA:\n Imidacloprid 10%\n\n"+                  
            "ESPECIES DE DESTINO: Felinos.",
            buttons: "Ver mas"
        });
    }
    
}
function producto(prod){
    
}