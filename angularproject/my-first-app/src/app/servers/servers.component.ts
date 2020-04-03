import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-servers',
  templateUrl: './servers.component.html',
  styleUrls: ['./servers.component.css']
})
export class ServersComponent implements OnInit {

  allowNewServer = false;
  createServer = "server was not created"
  serverName = 'test';
  serverCreated  = false;

  constructor() { 
    setTimeout(()=>{
    this.allowNewServer = true;
    },200)
  }

 

  
  
  ngOnInit() {
  }

  onCreateServer(){
    this.serverCreated = true;
    this.createServer ="server was created" + this.serverName
  }

  updateServerName(event:Event){
    console.log(event)
    this.serverName = (<HTMLInputElement>event.target).value;

  }

}
