import { AuthService } from './../services/auth.service';
import { Component, OnInit } from '@angular/core';
import { DiscussionService } from '../services/discussion.service';
import { NgbModal, NgbModalOptions } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-all-discussions',
  templateUrl: './all-discussions.component.html',
  styleUrls: ['./all-discussions.component.scss']
})
export class AllDiscussionsComponent implements OnInit {

  newDiscussion: any = {};
  discussions: any;
  modalReference: any;
  modalOptions: NgbModalOptions = {
    windowClass: 'in',
    backdrop: 'static',
    keyboard: false
  };

  constructor(
    private discussionService: DiscussionService,
    private modalService: NgbModal,
    private authService: AuthService,
  ) { }

  ngOnInit(): void {
    if(this.authService.isAuthenticated())
      this.discussionService.getDiscussions().subscribe((data)=>{
        this.discussions = data;
      });
  }

  close_modal() {
    this.modalReference.close();
  }

  open_modal(content) {
    this.modalReference = this.modalService.open(content, this.modalOptions);
  }

  closeModal(){
    this.newDiscussion = {};
    this.close_modal();
  }

  addDiscussion(){
    this.discussionService.createDiscussion(this.newDiscussion)
    .subscribe(
      (data)=>{
        this.discussions.unshift(data);
        this.closeModal();
      },
      (error)=>{
        console.log(error)

      }
    )
  }

  openDiscussionModal(content){
    this.open_modal(content);
  }

  getAuthService() {
    return this.authService;
  }
}
