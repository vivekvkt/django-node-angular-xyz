import { Component } from "@angular/core"


@Component({
    selector:'app-server',
    templateUrl:'./server.component.html'
})

export class ServerComponent {
    serverId:number= 10;
    sereverStatus:string = "offline";

    constructor(){
        this.sereverStatus = Math.random()> 0.5 ? 'online':'offline';
    }

    getServerStatus(){
        return this.sereverStatus
    }

    getColor(){
        return this.sereverStatus ==='online'? 'green':'red';
    }

}