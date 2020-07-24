import { Component, OnInit } from '@angular/core';
import { DiscussionService } from '../services/discussion.service';
import { Router, ActivatedRoute } from '@angular/router';
import { PostService } from '../services/post.service';

@Component({
  selector: 'app-discussions',
  templateUrl: './discussions.component.html',
  styleUrls: ['./discussions.component.scss']
})
export class DiscussionsComponent implements OnInit {

  discussion_id: number;
  discussion: any;
  posts: any = [];

  constructor(
    private discussionService: DiscussionService,
    private postService: PostService,
    private router: Router,
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.discussion_id = params['id'];
      this.getDiscussion();
    });
  }

  getDiscussion(){
    this.discussionService.getDiscussionDetail(this.discussion_id)
    .subscribe(
      (data)=>{
        this.discussion = data;
        this.posts = data.posts;
      },
      (error)=>{
        console.log(error);
      }
    )
  }
}
