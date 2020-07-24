import { Component, OnInit, Input } from '@angular/core';
import { NotificationService } from '../services/notification.service';

@Component({
  selector: 'app-notifications',
  templateUrl: './notifications.component.html',
  styleUrls: ['./notifications.component.scss']
})
export class NotificationsComponent implements OnInit {

  @Input() notifications: any;

  constructor(
    private notificationService: NotificationService
  ) { }

  ngOnInit(): void {
  }
}
