import { Component, OnInit } from '@angular/core';
import { AuthService } from './services/auth.service';
import { Router } from '@angular/router';
import { NotificationService } from './services/notification.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  model: any = {};
  user: any = {};
  isRegister: boolean = false;
  isShowNotificationPopup: boolean = false;
  notifications: any = [];

  constructor(
    private authService: AuthService,
    private router: Router,
    private notificationService: NotificationService
  ){
    if(authService.isAuthenticated()){
      notificationService.messages.subscribe(msg => {
        this.notifications.unshift(msg.message);
      });
    }
  }

  ngOnInit(){
    // this.redirect();
    if(this.authService.isAuthenticated()){
      this.getAllNotification();
    }
  }

  redirect(){
    if(this.authService.isAuthenticated())
      this.router.navigate(["discussions"]);
  }

  login(){
    this.authService.login(this.model)
    .subscribe((res)=>{
      localStorage.setItem('authToken', res.token);
      localStorage.setItem('username', res.username);
      window.location.reload();
    },
    (err)=>{

    });
  }

  registration(){
    this.authService.register(this.user)
    .subscribe((res)=>{
      localStorage.setItem('authToken', res.token);
      localStorage.setItem('username', res.username);
      window.location.reload();
    })
  }

  getAllNotification(){
    this.notificationService.getNotifications()
    .subscribe(
      (data) => { 
        this.notifications = data;
      },
      (error) => {
        console.log(error);
      }
    )
  }

  logout(){
    localStorage.removeItem('authToken');
    localStorage.removeItem('username');
    window.location.reload();
  }

  getAuthService() {
    return this.authService;
  }

}
