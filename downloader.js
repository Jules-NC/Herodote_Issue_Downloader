"use strict"
function downloadIssue(){
    let elements = document.getElementsByClassName("btn btn-default")
    let articles_ids = []
    let articles_pdfs = []
    for(let i = 2; i<elements.length; i+=3){
        articles_ids.push(elements[i].getAttribute("data-id_article"))
    }
    for(id of articles_ids){
        window.open('./load_pdf.php?ID_ARTICLE='+id+'&download=1')
        articles_pdfs.push('./load_pdf.php?ID_ARTICLE='+id+'.pdf')
    }
}

downloadIssue()
