import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { CommonModule } from '@angular/common';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AllDiscussionsComponent } from './all-discussions/all-discussions.component';
import { DiscussionsComponent } from './discussions/discussions.component';
import { PostsComponent } from './posts/posts.component';
import { NotificationsComponent } from './notifications/notifications.component';
import { AuthService } from './services/auth.service';
import { DiscussionService } from './services/discussion.service';
import { PostService } from './services/post.service';
import { NotificationService } from './services/notification.service';
import { TokenInterceptor } from './services/token-interceptor';
import { WebsocketService } from './services/websocket.service';

@NgModule({
  declarations: [
    AppComponent,
    AllDiscussionsComponent,
    DiscussionsComponent,
    PostsComponent,
    NotificationsComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    CommonModule,
    HttpClientModule,
    NgbModule
  ],
  providers: [
    {
      provide : HTTP_INTERCEPTORS,
      useClass: TokenInterceptor,
      multi   : true,
    },
    AuthService,
    DiscussionService,
    PostService,
    NotificationService,
    WebsocketService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
