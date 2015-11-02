var gulp = require('gulp');

var coffee = require('gulp-coffee');
var coffeelint = require('gulp-coffeelint');
var gutil = require('gulp-util');
var less = require('gulp-less');
var recess = require('gulp-recess');
var uglify = require('gulp-uglify');
var uglifycss = require('gulp-uglifycss');

// Lint coffeescripts
gulp.task('lint-coffee', function() {
    return gulp.src('*/static/**/*.coffee')
        .pipe(coffeelint())
        .pipe(coffeelint.reporter('default'));
});

// Lint less
gulp.task('lint-less', function () {
    return gulp.src('*/static/**/*.less')
        .pipe(recess())
        .pipe(recess.reporter());
});

// Compile less to css
gulp.task('less', function() {
    return gulp.src('*/static/**/*.less')
        .pipe(less())
        .pipe(gulp.dest('.'));
});

// Minify CSS
gulp.task('minify-css', function() {
    return gulp.src('*/static/**/*.css')
        .pipe(uglifycss())
        .pipe(gulp.dest('.'));
});

// Convert coffee to JS
gulp.task('coffee', function() {
    return gulp.src('*/static/**/*.coffee')
        .pipe(coffee({bare: true}).on('error', gutil.log))
        .pipe(gulp.dest('.'))
});

// Minify JS
gulp.task('minify-js', function() {
    return gulp.src('*/static/**/*.js')
        .pipe(uglify())
        .pipe(gulp.dest('.'));
});

// Build coffee
gulp.task('coffee-build', ['lint-coffee', 'coffee', 'minify-js']);

// Build css
gulp.task('less-build', ['lint-less', 'less', 'minify-css']);

// Watch Files For Changes
gulp.task('watch', function() {
    gulp.watch('*/static/**/*.coffee', ['coffee-build']);
    gulp.watch('*/static/**/*.less', ['less-build']);
});

// Build coffee and css
gulp.task('check-and-build', ['coffee-build', 'less-build']);

// Default Task
gulp.task('default', ['check-and-build', 'watch']);
