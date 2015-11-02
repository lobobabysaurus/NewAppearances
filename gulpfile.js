var gulp = require('gulp');

var clean = require('gulp-clean');
var coffee = require('gulp-coffee');
var coffeelint = require('gulp-coffeelint');
var gutil = require('gulp-util');
var less = require('gulp-less');
var uglify = require('gulp-uglify');
var uglifycss = require('gulp-uglifycss');


var jsDir = '*/static/**/*.js';
var coffeeDir = '*/static/**/*.coffee';
var cssDir = '*/static/**/*.css';
var lessDir = '*/static/**/*.less';

//Clean old JS
gulp.task('clean-js', function () {
  return gulp.src(jsDir, {read: false})
    .pipe(clean());
});

// Lint Coffeescript
gulp.task('lint-coffee', function() {
    return gulp.src(coffeeDir)
        .pipe(coffeelint())
        .pipe(coffeelint.reporter('default'));
});

// Convert Coffeescript to JS
gulp.task('coffee', function() {
    return gulp.src(coffeeDir)
        .pipe(coffee({bare: true}).on('error', gutil.log))
        .pipe(gulp.dest('.'))
});

// Minify JS
gulp.task('minify-js', function() {
    return gulp.src(jsDir)
        .pipe(uglify())
        .pipe(gulp.dest('.'));
});

// Clean CSS
gulp.task('clean-css', function () {
  return gulp.src(cssDir, {read: false})
    .pipe(clean());
});

// Lint Less
gulp.task('lint-less', function () {
    return gulp.src(lessDir)
        .pipe(recess())
        .pipe(recess.reporter());
});

// Compile Less to CSS
gulp.task('less', function() {
    return gulp.src(lessDir)
        .pipe(less())
        .pipe(gulp.dest('.'));
});

// Minify CSS
gulp.task('minify-css', function() {
    return gulp.src(cssDir)
        .pipe(uglifycss())
        .pipe(gulp.dest('.'));
});

// Build coffee
gulp.task('coffee-build', ['clean-js', 'lint-coffee', 'coffee', 'minify-js']);

// Build css
gulp.task('less-build', ['clean-css', 'lint-less', 'less', 'minify-css']);

// Watch Files For Changes
gulp.task('watch', function() {
    gulp.watch(coffeeDir, ['coffee-build']);
    gulp.watch(lessDir, ['less-build']);
});

// Build coffee and css
gulp.task('clean-check-and-build', ['coffee-build', 'less-build']);

// Default Task
gulp.task('default', ['check-and-build', 'watch']);
