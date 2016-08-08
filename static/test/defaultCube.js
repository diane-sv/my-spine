window.onload = function() {
  var r1 = new X.renderer3D();
  r1.container = 'main3d';
  r1.bgColor = [.62, .62, 1];
  r1.init();

  var obj_cube = new X.cube();
  obj_cube.texture.file = 'http://www.wired.com/wp-content/uploads/2014/07/brain1.jpg';

  r1.add(obj_cube);
  r1.render();


  var r2 = new X.renderer3D();
  r2.container = 'sliceX';
  r2.bgColor = [.62, .62, 1];
  r2.init();

  var obj2_cube = new X.cube();
  obj2_cube.color = [0,0,1];
  
  r2.add(obj2_cube);
  r2.render();


  var r3 = new X.renderer3D();
  r3.container = 'sliceY';
  r3.bgColor = [.62, .62, 1];
  r3.init();

  var obj3_cube = new X.cylinder();
  obj3_cube.color = [1,1,0];
  
  r3.add(obj3_cube);
  r3.render();


  var r4 = new X.renderer3D();
  r4.container = 'sliceZ';
  r4.bgColor = [.62, .62, 1];
  r4.init();

  var obj4_cube = new X.cube();
  obj4_cube.color = [0,.5,.5];
  
  r4.add(obj4_cube);
  r4.render();

};
