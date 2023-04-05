function getlocation()
{
  var name = localStorage.getItem("rno"); 
  var busnumber = localStorage.getItem("busnumber"); 

  console.log(name);
  $.ajax({
    url: "//.{% url 'demo' %}",
    type: 'POST',
    data : {
      name:name,
      busnumber : busnumber,
      csrfmiddlewaretoken: '{{ csrf_token }}'
    },
    success: (data) => {
      console.log(data);
    },
    error: (error) => {
      console.log(error);
    }
  });
}