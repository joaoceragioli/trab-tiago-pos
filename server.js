function submit() {
    var ajax = new XMLHttpRequest();
    
    // Seta tipo de requisição: Post e a URL da API
    ajax.open("POST", "https://trab-tiago-pos.herokuapp.com/ocrdobigas", true);
    ajax.setRequestHeader("Content-type", "application/json");
    
    // Seta paramêtros da requisição e envia a requisição
    ajax.send({
        "text": "bigas"
    });
    
    // Cria um evento para receber o retorno.
    ajax.onreadystatechange = function() {
      
      // Caso o state seja 4 e o http.status for 200, é porque a requisiçõe deu certo.
        if (ajax.readyState == 4 && ajax.status == 200) {
        
            var data = ajax.responseText;
            
        // Retorno do Ajax
            console.log(data);
        }
    }
}