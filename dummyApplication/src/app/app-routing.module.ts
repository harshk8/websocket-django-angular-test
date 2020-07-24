import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AllDiscussionsComponent } from './all-discussions/all-discussions.component';
import { DiscussionsComponent } from './discussions/discussions.component';
import { PostsComponent } from './posts/posts.component';


const routes: Routes = [  
  {
    path: '',
    component: AllDiscussionsComponent,

  },
  {
    path: 'discussions',
    component: AllDiscussionsComponent,
  },
  {
    path: 'discussions/:id',
    component: DiscussionsComponent,
  },
  {
    path: 'discussions/:id/posts',
    component: PostsComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
