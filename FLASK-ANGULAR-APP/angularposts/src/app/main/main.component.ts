import { Component, OnInit, OnDestroy } from '@angular/core';
import { FlaskapiService } from '../flaskapi.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit, OnDestroy {

  constructor(
    private flaskApiService: FlaskapiService
  ) { }

  public posts: any[];
  public postSubscription: Subscription;
  public imageURL: string;

  public getPosts() {
    this.postSubscription = this.flaskApiService.getPosts()
      .subscribe(
        p => {
          // tslint:disable-next-line: no-string-literal
          this.posts = p['data'];
          console.log(this.posts);
    });
  }

  public getImage(imageName: string): string {
    this.imageURL = this.flaskApiService.getImage(imageName);
    return this.imageURL;
  }

  ngOnInit(): void {
    this.getPosts();
  }
  ngOnDestroy() {
    this.postSubscription.unsubscribe();
  }

}
