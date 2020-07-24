import { Injectable } from '@angular/core';
import { AbstractService } from './abstract.service';
import { Observable } from 'rxjs';
import { WebsocketService } from './websocket.service';
import {Subject} from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { AuthService } from './auth.service';
import * as Rx from 'rxjs'

export interface Message {
  author: string;
  message: string;
}
@Injectable()
export class NotificationService extends AbstractService {
  public messages;

  constructor(
    private wsService: WebsocketService,
    http: HttpClient,
    private authService: AuthService
  ){
    super(http);
    if(authService.isAuthenticated())
      this.messages = <Subject<Message>>wsService.connect('ws://localhost:8000/ws/chat/notification_'+ authService.getUsername() + '/').map(
        (response: MessageEvent): Message => {
          let data = JSON.parse(response.data);
          return data
        }
      );
  }


  getNotifications(): Observable<any>{
    return this.get('http://localhost:8000/notification/');
  }

  createNotification(notification): Observable<any>{
    return this.post('url', notification);
  }

  getNotificationDetail(notification_id): Observable<any>{
    return this.get('url');
  }
}