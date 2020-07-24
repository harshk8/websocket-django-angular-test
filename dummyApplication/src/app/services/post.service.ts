import { Injectable } from '@angular/core';
import { AbstractService } from './abstract.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PostService extends AbstractService {

  getPosts(discussion_id): Observable<any>{
    return this.get('http://localhost:8000/forum/discussion/'+discussion_id+'/posts/');
  }

  createPost(post): Observable<any>{
    return this.post('http://localhost:8000/forum/post/', post);
  }

  getPostDetail(post_id): Observable<any>{
    return this.get('url');
  }
}