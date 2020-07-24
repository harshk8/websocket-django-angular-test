import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { AbstractService } from './abstract.service';

@Injectable({
  providedIn: 'root'
})
export class AuthService extends AbstractService{
  authToken: string;
  username: string; 
  
  constructor(http: HttpClient){
    super(http)
  }

  private getAuth(): any {
    if (!this.authToken) {
      this.authToken = localStorage.getItem('authToken');
    }
    return this.authToken;
  }

  register(user): Observable<any>{
    return this.post('http://localhost:8000/user/register/', user);
  }

  login(user): Observable<any>{
    return this.post('http://localhost:8000/user/login/', user);
  }

  isAuthenticated(): boolean{
    if(this.getAuth()){
      return true;
    }else{
      return false;
    }
  }

  getAuthToken(): string{
    return this.getAuth();
  }

  getUsername(): string{
    if(!this.username){
      this.username = localStorage.getItem('username');
    }
    return this.username;
  }

}
