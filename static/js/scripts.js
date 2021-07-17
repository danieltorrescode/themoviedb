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

// console.log( request('','',''))