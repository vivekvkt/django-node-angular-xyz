import { Component ,ElementRef, ViewChild} from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  @ViewChild('f') signupform:NgForm
  defualtQuestion=  'pet'
  answer='';
  genders = ['male', 'female'];

  user={
    username:'',
    email:'',
    secretQuestion:'',
    answer:'',
    gender:''
  }
submitted = false
  suggestUserName(){
    const suggestedName = "superuser"
    // this.signupform.setValue( {
    //   userData:{
    //     username:suggestedName,
    //     email:''
    //   },
    //   secret:'pet',
    //   questionAnswer:'',
    //   gender:'male'
    // })
    this.signupform.form.patchValue({
      userData:{
        username:suggestedName,

      }
    })
  }

  // onSubmit(form:NgForm){
  // console.log("submited here", form)
  // }

  onSubmit(){
    //console.log("submited here",this.signupform)
    this.submitted = true;
    this.user.username =  this.signupform.value.userData.username;
    this.user.email =  this.signupform.value.userData.email;
    this.user.secretQuestion = this.signupform.value.secret;
    this.user.answer = this.signupform.value.questionAnswer;
    this.user.gender  = this.signupform.value.gender;
    this.signupform.reset()
    }
}
