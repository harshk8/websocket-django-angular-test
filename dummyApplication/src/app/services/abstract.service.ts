import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';

@Injectable()
export abstract class AbstractService {
  constructor(private http: HttpClient) {}

  get(url: string, config: object = {}): Observable<any> {
    return this.http.get(url, this.mergeConfig(config));
  }

  post(url: string, data: any, config: object = {}): Observable<any> {
    return this.http.post(url, data, this.mergeConfig(config));
  }

  patch(url: string, data: any, config: object = {}): Observable<any> {
    return this.http.patch(url, data, this.mergeConfig(config));
  }

  put(url: string, data: any, config: object = {}): Observable<any> {
    return this.http.put(url, data, this.mergeConfig(config));
  }

  delete(url: string, config: object = {}): Observable<any> {
    return this.http.delete(url, this.mergeConfig(config));
  }

  client(): HttpClient {
    return this.http;
  }

  private mergeConfig(config): object {
    const defaults = {
      observe: 'body',
      responseType: 'json',
      'Content-Type':'application/json; charset=utf-8'
    };

    return { ...defaults, ...config };
  }
}
