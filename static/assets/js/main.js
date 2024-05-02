
import { SubscriptionToHellfireClub } from "./firebase/hellfire-clube.js";



const txtName = document.getElementById("txtName");
const txtEmail = document.getElementById("txtEmail");
const txtLevel = document.getElementById("txtLevel");
const txtCharacter = document.getElementById("txtCharacter");
const btnSubscribe = document.getElementById("btnSubscribe");

btnSubscribe.addEventListener("click",async () => {
  const Subscription = {
    name: txtName.value,
    email: txtEmail.value,
    lavel: txtLevel.value,
    character: txtCharacter.value,
  };

 const SubscriptionId = await SubscriptionToHellfireClub(Subscription)
 console.log(`inscrito com sucesso:${SubscriptionId}`)

 txtName.value =''
 txtEmail.value =''
 txtLevel.value =''
 txtCharacter.value =''
  
 alert(`inscrito com sucesso: Seu ID é :${SubscriptionId}`)
});


document.getElementById('btnSubscribe').addEventListener('click', function() {
  // Capturar os valores dos campos do formulário
  var name = document.getElementById('txtName').value;
  var email = document.getElementById('txtEmail').value;
  var restaurant = document.getElementById('restaurant').value;
  var character = document.getElementById('txtCharacter').value;

  // Montar os dados para enviar por email
  var data = {
      name: name,
      email: email,
      restaurant: restaurant,
      character: character
  };

  // Enviar os dados para o servidor
  sendDataToServer(data);
});
