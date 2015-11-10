gulp = require('gulp')

clean = require('gulp-clean')
coffee = require('gulp-coffee')
coffeelint = require('gulp-coffeelint')
gutil = require('gulp-util')
less = require('gulp-less')
recess = require('gulp-recess')
uglify = require('gulp-uglify')
uglifycss = require('gulp-uglifycss')
runSequence = require('run-sequence')

dirs =
  js: '*/static/**/*.js'
  coffee: '*/static/**/*.coffee'
  css: '*/static/**/*.css'
  less:  '*/static/**/*.less'

# Clean old JS
gulp.task 'clean-js', ->
  return gulp.src(dirs.js, read: false)
    .pipe(clean())

# Lint Coffeescript
gulp.task 'lint-coffee', ->
  return gulp.src(dirs.coffee)
    .pipe(coffeelint())
    .pipe(coffeelint.reporter('default'))

# Convert Coffeescript to JS
gulp.task 'coffee-to-js', ->
  return gulp.src(dirs.coffee)
    .pipe(coffee(bare: true).on('error', gutil.log))
    .pipe(gulp.dest('.'))

# Minify JS
gulp.task 'minify-js', ->
  return gulp.src(dirs.js)
    .pipe(uglify())
    .pipe(gulp.dest('.'))

# Clean CSS
gulp.task 'clean-css', ->
  return gulp.src(dirs.css, read: false)
    .pipe(clean())

# Lint Less
gulp.task 'lint-less', ->
  return gulp.src(dirs.less)
    .pipe(recess())
    .pipe(recess.reporter())

# Compile Less to CSS
gulp.task 'less', ->
  return gulp.src(dirs.less)
    .pipe(less())
    .pipe(gulp.dest('.'))


# Minify CSS
gulp.task 'minify-css', ->
  return gulp.src(dirs.css)
    .pipe(uglifycss())
    .pipe(gulp.dest('.'))

# Build coffee
gulp.task 'build-coffee', ->
  return runSequence('clean-js', 'lint-coffee', 'coffee-to-js', 'minify-js')

# Build css
gulp.task 'build-less', ->
  return runSequence('clean-css', 'lint-less', 'less', 'minify-css')

# Watch Files For Changes
gulp.task 'watch', ->
  gulp.watch dirs.coffee, ['build-coffee']
  gulp.watch dirs.less, ['build-less']

# Build coffee and css
gulp.task 'build-both', ['build-coffee', 'build-less']

# Default Task
gulp.task 'default', ->
  return runSequence('build-both', 'watch')
