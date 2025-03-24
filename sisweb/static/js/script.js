function regraDaEscolha() {
    var category = document.getElementById("category").value;
    var nameField = document.getElementById("nameField");
    var matriculaField = document.getElementById("matriculaField");
    var turmaA = document.getElementById("turmaA");
    var turmaB = document.getElementById("turmaB");
    var turmaC = document.getElementById("turmaC");
    var anoField = document.getElementById("anoField");

    anoField.style.display = "none";
    turmaA.style.display = "none";
    turmaB.style.display = "none";
    turmaC.style.display = "none";
  
    if (category === "alunoEspecifico") {
      nameField.style.display = "block";  // Exibe os campos quando "Específico" for selecionado
      matriculaField.style.display = "block";
      anoField.style.display = "none";

    }else if(category === "categorias") {
        nameField.style.display = "none";  // Oculta os campos quando "Geral" for selecionado
        matriculaField.style.display = "none";
        anoField.style.display = "none"; 
      } else {
      nameField.style.display = "none";  // Oculta os campos quando "Geral" for selecionado
      matriculaField.style.display = "none";
      anoField.style.display = "block"; 
    }
  }


function surgirTurmas() {
    var anoField = document.getElementById("ano").value;
    var turmaA = document.getElementById("turmaA");
    var turmaB = document.getElementById("turmaB");
    var turmaC = document.getElementById("turmaC");
  
    if (anoField === "anoGeral") {
        turmaA.style.display = "block";  // Exibe os campos quando "Específico" for selecionado
        turmaB.style.display = "block";
        turmaC.style.display = "block";

    }else{
        turmaA.style.display = "none";
        turmaB.style.display = "none";
        turmaC.style.display = "none";
    }
  }


  function turmaA() {
    var anoField = document.getElementById("ano").value;
    var turmaA = document.getElementById("turmaA");
    var turmaB = document.getElementById("turmaB");
    var turmaC = document.getElementById("turmaC");
  
    if (anoField === "anoGeral") {
        turmaA.style.display = "block";  // Exibe os campos quando "Específico" for selecionado
        turmaB.style.display = "block";
        turmaC.style.display = "block";

    }else{
        turmaA.style.display = "none";
        turmaB.style.display = "none";
        turmaC.style.display = "none";
    }
  }

