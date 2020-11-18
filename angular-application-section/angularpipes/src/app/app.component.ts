import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
 servers =[
   {
     instanceType:'medium',
     name :'Production Server',
     status:'stable',
     started: new  Date(15,10,2020)
   },
   {
    instanceType:'medium',
    name :'Production Server',
    status:'stable',
    started: new  Date(15,10,2020)
  },
  {
    instanceType:'medium',
    name :'Production Server',
    status:'stable',
    started: new  Date(15,10,2020)
  }
 ];

 getStatusClasses(server:{instanceType:string,name:string,status:string,started:Date}){
    return {
        'list-group-item-success':server.status==='stable',
        'list-group-item-warning':server.status==='offline',
        'list-group-item-danger':server.status==='critical',
    }
 }
}
