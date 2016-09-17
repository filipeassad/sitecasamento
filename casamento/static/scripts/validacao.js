function validar() {

    var nome = form1.nome.value;
    var pessoas = form1.pessoas.value;

    if (nome == "") {
        alert('Preencha o nome!');
        form1.nome.focus();
        return false;
    }

    if (pessoas == "") {
        alert('Preencha o numero de pessoas!');
        form1.pessoas.focus();
        return false;
    }
}