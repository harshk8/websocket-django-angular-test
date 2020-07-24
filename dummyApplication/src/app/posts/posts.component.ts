import { Component, OnInit, Input, SimpleChanges } from '@angular/core';
import { PostService } from '../services/post.service';
import { NgbModal, NgbModalOptions } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.scss']
})
export class PostsComponent implements OnInit {

  @Input() posts: any;
  @Input() discussion_id: any;
  newPost: any = {};
  modalReference: any;
  modalOptions: NgbModalOptions = {
    windowClass: 'in',
    backdrop: 'static',
    keyboard: false
  };

  constructor(
    private postService: PostService,
    private modalService: NgbModal,
  ) { }

  ngOnInit(): void {
    
  }

  ngOnChanges(changes: SimpleChanges) {
    if ('posts' in changes) {
      this.posts = changes.posts.currentValue;
    }
} 

  close_modal() {
    this.modalReference.close();
  }

  open_modal(content) {
    this.modalReference = this.modalService.open(content, this.modalOptions);
  }

  closeModal(){
    this.newPost = {};
    this.close_modal();
  }

  addPost(){
    this.newPost.discussion = this.discussion_id;
    this.postService.createPost(this.newPost)
    .subscribe(
      (data)=>{
        this.posts.unshift(data);
        this.closeModal();
      },
      (error)=>{
        console.log(error)
      }
    )
  }

  openPostModal(content){
    this.open_modal(content);
  }

}
