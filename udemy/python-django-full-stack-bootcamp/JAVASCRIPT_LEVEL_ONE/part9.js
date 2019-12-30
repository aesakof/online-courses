var firstName = prompt("Enter your first name")
var lastName = prompt("Enter your last name")
var age = prompt("Enter your age")
var height = prompt("Enter your height (in centimeters)")
var petName = prompt("Enter your pet name")

if(firstName[0] == lastName[0]) {
  if(age > 20 && age < 30) {
    if(height >= 170) {
      if(petName[petName.length - 1] == 'y') {
        console.log("All spy conditions met")
      }
    }
  }
}
