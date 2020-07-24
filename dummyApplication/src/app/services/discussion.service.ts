import { Injectable } from '@angular/core';
import { AbstractService } from './abstract.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DiscussionService extends AbstractService {

  getDiscussions(): Observable<any>{
    return this.get('http://localhost:8000/forum/discussion/');
  }

  createDiscussion(discussion): Observable<any>{
    return this.post('http://localhost:8000/forum/discussion/', discussion);
  }

  getDiscussionDetail(discussion_id): Observable<any>{
    return this.get('http://localhost:8000/forum/discussion/'+discussion_id+'/');
  }
}
