//alert("$$$$$$$$$$$$$$$$");


function request(method,resource,data) {
  let url = `${this.url}${resource}`

  let body = {}

  if ( JSON.stringify(data) != '{}' ){
      body ={
          body: JSON.stringify(data)
      }
  }

  let content = {
      method: method,
      headers:{
          'Content-Type': 'application/json',
          ...this.fetchHeaders
      },
      ...body,
      ...this.fetchContent
  }

  return fetch(url,content).then(
      res => this.checkResponse(res)
  )
  .then(resp => resp)
  .catch(error => {
      console.error('Error:', error)
      this.showMessage(error,"error")
  });

}


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
  let baseUrl = 'http://127.0.0.1:8000';
  let url = `${ baseUrl }/${ resource }/${ element.value }`;

  window.location.href = encodeURI(url);

  // fetch('http://127.0.0.1:8000/movie/details/'+element.value)
  // .then(response => response.json()
  // )
  // .then(data => console.log(data));

}
