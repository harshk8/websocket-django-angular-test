import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AllDiscussionsComponent } from './all-discussions.component';

describe('AllDiscussionsComponent', () => {
  let component: AllDiscussionsComponent;
  let fixture: ComponentFixture<AllDiscussionsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AllDiscussionsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AllDiscussionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
