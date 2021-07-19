// constants
const BASE_URL =  'http://127.0.0.1:8000'

// function in charge of make the get call to the django
// that allows the search with filters
function changeHandler(id){
  let element = document.getElementById(id);
  // Simulate a mouse click:
  let resource = '';
  if(id === 'name'){
    resource = 'show';
  }else if (id === 'first_air_date') {
    resource = 'releases';
  }else if (id === 'popularity') {
    resource = 'popularity';
  } else {
    resource = '';
  }
  let url = `${ BASE_URL }/${ resource }/${ element.value }`;
  window.location.href = encodeURI(url);
}

// function that handle the simple paginator
function changePage(page){
  if(page <= 0 ){
    window.location.href = BASE_URL;
  }else{

    let baseUrl = window.location.href;
    baseUrl = baseUrl.split('?');
    baseUrl = baseUrl[0];
    window.location.href = encodeURI(`${ baseUrl }?page=${ page }`);
  }
}

function rating(id,tv_id){

  let element = document.getElementById(id);
  let value = element.value;
  if(isNaN(value)){
    alert('rating value is not a valid number')
    return false
  }
  if(value < 0.5 || value > 10){
    alert('rating value is not a valid number')
    return false
  }

  let csrf_token = document.getElementById('csrf_token');
  csrf_token = csrf_token.lastElementChild.value
  const data = { 'value' : value, 'tv_id': tv_id };

  fetch(`${ BASE_URL }/rating/`, {
    method: 'POST', // or 'PUT'
    headers: {
      'Content-Type': 'application/json',
      "X-CSRFToken": csrf_token
    },
    body: JSON.stringify(data),
  })
  .then(response => response.json())
  .then(data => {
    console.log('success:', data.success);
    console.log('status_code:', data.status_code);
    console.log('status_message:', data.status_message);
    alert(data.status_message)
  })

}